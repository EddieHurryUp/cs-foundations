import { useEffect, useMemo, useState } from 'react';
import { marked } from 'marked';

const DEFAULT_PATH = 'notes/00-overview/learning-map.md';

const groupLabel = (group) => {
  if (group === 'notes') return '学习笔记';
  if (group === 'index') return '索引';
  if (group === 'root') return '根目录';
  return group;
};

const normalize = (value) => value?.toLowerCase() ?? '';

const buildTree = (entries, rootPrefix) => {
  const root = { name: rootPrefix ?? '', path: rootPrefix ?? '', children: [] };
  const insert = (entry) => {
    const parts = entry.path.split('/');
    const normalizedParts = rootPrefix ? parts.slice(1) : parts;
    let cursor = root;
    let accumulated = rootPrefix ?? '';
    normalizedParts.forEach((part, index) => {
      const isFile = part.endsWith('.md');
      accumulated = accumulated ? `${accumulated}/${part}` : part;
      let child = cursor.children.find((node) => node.name === part);
      if (!child) {
        child = { name: part, path: accumulated, children: [], entry: null };
        cursor.children.push(child);
      }
      if (isFile && index === normalizedParts.length - 1) {
        child.entry = entry;
      }
      cursor = child;
    });
  };

  entries.forEach(insert);

  const sortNodes = (nodes) => {
    nodes.sort((a, b) => a.name.localeCompare(b.name, 'zh-Hans-CN'));
    nodes.forEach((node) => sortNodes(node.children));
  };
  sortNodes(root.children);
  return root.children;
};

const TreeNode = ({ node, depth, activePath, onSelect }) => {
  const indent = { paddingLeft: `${depth * 16}px` };
  if (node.entry) {
    return (
      <button
        className={activePath === node.entry.path ? 'nav-item active' : 'nav-item'}
        style={indent}
        onClick={() => onSelect(node.entry.path)}
      >
        {node.entry.title}
      </button>
    );
  }

  return (
    <div className="tree-node">
      <div className="tree-label" style={indent}>
        {node.name.replace('.md', '')}
      </div>
      {node.children.map((child) => (
        <TreeNode
          key={child.path}
          node={child}
          depth={depth + 1}
          activePath={activePath}
          onSelect={onSelect}
        />
      ))}
    </div>
  );
};

export default function App() {
  const [manifest, setManifest] = useState([]);
  const [activePath, setActivePath] = useState(DEFAULT_PATH);
  const [content, setContent] = useState('');
  const [status, setStatus] = useState('loading');
  const [query, setQuery] = useState('');
  const [selectedTag, setSelectedTag] = useState('all');

  useEffect(() => {
    const loadManifest = async () => {
      try {
        const res = await fetch('content/manifest.json');
        if (!res.ok) throw new Error('manifest load failed');
        const data = await res.json();
        setManifest(data);
      } catch (err) {
        setManifest([]);
      }
    };
    loadManifest();
  }, []);

  useEffect(() => {
    const loadContent = async () => {
      setStatus('loading');
      try {
        const res = await fetch(`content/${activePath}`);
        if (!res.ok) throw new Error('content load failed');
        const text = await res.text();
        setContent(marked.parse(text));
        setStatus('ready');
      } catch (err) {
        setContent('加载失败，请确认内容已同步。');
        setStatus('error');
      }
    };
    loadContent();
  }, [activePath]);

  const tags = useMemo(() => {
    const tagSet = new Set();
    manifest.forEach((entry) => {
      (entry.tags || []).forEach((tag) => tagSet.add(tag));
    });
    return Array.from(tagSet).sort((a, b) => a.localeCompare(b));
  }, [manifest]);

  const filtered = useMemo(() => {
    const q = normalize(query.trim());
    return manifest.filter((entry) => {
      const inTag = selectedTag === 'all' || (entry.tags || []).includes(selectedTag);
      const inText =
        !q ||
        normalize(entry.title).includes(q) ||
        normalize(entry.path).includes(q);
      return inTag && inText;
    });
  }, [manifest, query, selectedTag]);

  const grouped = useMemo(() => {
    const map = new Map();
    filtered.forEach((entry) => {
      if (!map.has(entry.group)) map.set(entry.group, []);
      map.get(entry.group).push(entry);
    });
    return Array.from(map.entries()).map(([group, entries]) => ({
      group,
      entries
    }));
  }, [filtered]);

  const notesTree = useMemo(() => {
    const notesEntries = filtered.filter((entry) => entry.group === 'notes');
    return buildTree(notesEntries, 'notes');
  }, [filtered]);

  const indexTree = useMemo(() => {
    const indexEntries = filtered.filter((entry) => entry.group === 'index');
    return buildTree(indexEntries, 'index');
  }, [filtered]);

  const rootEntries = grouped.find((g) => g.group === 'root')?.entries ?? [];

  return (
    <div className="app">
      <aside className="sidebar">
        <div className="brand">
          <div className="badge">cs-foundations</div>
          <h1>知识库导航</h1>
          <p>浏览 Markdown 内容并保持同步。</p>
        </div>

        <button
          className="primary"
          onClick={() => setActivePath(DEFAULT_PATH)}
        >
          返回学习地图
        </button>

        <div className="filter">
          <input
            className="search"
            placeholder="搜索标题或路径"
            value={query}
            onChange={(event) => setQuery(event.target.value)}
          />
          <div className="tag-list">
            <button
              className={selectedTag === 'all' ? 'tag active' : 'tag'}
              onClick={() => setSelectedTag('all')}
            >
              全部
            </button>
            {tags.map((tag) => (
              <button
                key={tag}
                className={selectedTag === tag ? 'tag active' : 'tag'}
                onClick={() => setSelectedTag(tag)}
              >
                {tag}
              </button>
            ))}
          </div>
        </div>

        <div className="nav">
          {filtered.length === 0 ? (
            <p className="muted">未找到匹配内容。</p>
          ) : (
            <>
              <div className="section">
                <h2>{groupLabel('notes')}</h2>
                {notesTree.map((node) => (
                  <TreeNode
                    key={node.path}
                    node={node}
                    depth={0}
                    activePath={activePath}
                    onSelect={setActivePath}
                  />
                ))}
              </div>
              <div className="section">
                <h2>{groupLabel('index')}</h2>
                {indexTree.map((node) => (
                  <TreeNode
                    key={node.path}
                    node={node}
                    depth={0}
                    activePath={activePath}
                    onSelect={setActivePath}
                  />
                ))}
              </div>
              {rootEntries.length > 0 && (
                <div className="section">
                  <h2>{groupLabel('root')}</h2>
                  {rootEntries.map((entry) => (
                    <button
                      key={entry.path}
                      className={
                        activePath === entry.path
                          ? 'nav-item active'
                          : 'nav-item'
                      }
                      onClick={() => setActivePath(entry.path)}
                    >
                      {entry.title}
                    </button>
                  ))}
                </div>
              )}
            </>
          )}
        </div>
      </aside>

      <main className="content">
        <header className="content-header">
          <div>
            <span className="label">当前文档</span>
            <h2>{activePath}</h2>
          </div>
          <span className={`status ${status}`}>{status}</span>
        </header>
        <article
          className="markdown"
          dangerouslySetInnerHTML={{ __html: content }}
        />
      </main>
    </div>
  );
}
