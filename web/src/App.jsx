import { useEffect, useMemo, useState } from 'react';
import { marked } from 'marked';

const DEFAULT_PATH = 'notes/00-overview/learning-map.md';

const groupLabel = (group) => {
  if (group === 'notes') return '学习笔记';
  if (group === 'index') return '索引';
  if (group === 'root') return '根目录';
  return group;
};

const sortEntries = (entries) =>
  [...entries].sort((a, b) => a.title.localeCompare(b.title, 'zh-Hans-CN'));

export default function App() {
  const [manifest, setManifest] = useState([]);
  const [activePath, setActivePath] = useState(DEFAULT_PATH);
  const [content, setContent] = useState('');
  const [status, setStatus] = useState('loading');

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

  const groups = useMemo(() => {
    const grouped = new Map();
    manifest.forEach((entry) => {
      if (!grouped.has(entry.group)) grouped.set(entry.group, []);
      grouped.get(entry.group).push(entry);
    });
    return Array.from(grouped.entries()).map(([group, entries]) => ({
      group,
      entries: sortEntries(entries)
    }));
  }, [manifest]);

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
        <div className="nav">
          {groups.length === 0 ? (
            <p className="muted">未找到目录索引，请先同步内容。</p>
          ) : (
            groups.map((section) => (
              <div key={section.group} className="section">
                <h2>{groupLabel(section.group)}</h2>
                {section.entries.map((entry) => (
                  <button
                    key={entry.path}
                    className={
                      activePath === entry.path ? 'nav-item active' : 'nav-item'
                    }
                    onClick={() => setActivePath(entry.path)}
                  >
                    {entry.title}
                  </button>
                ))}
              </div>
            ))
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
