import { readdir, readFile, writeFile } from 'node:fs/promises';
import { dirname, extname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const contentRoot = join(__dirname, '..', 'public', 'content');
const outputPath = join(contentRoot, 'manifest.json');

const walk = async (dir, prefix = '') => {
  const entries = await readdir(dir, { withFileTypes: true });
  const files = [];
  for (const entry of entries) {
    const full = join(dir, entry.name);
    const rel = join(prefix, entry.name);
    if (entry.isDirectory()) {
      files.push(...(await walk(full, rel)));
    } else if (extname(entry.name) === '.md') {
      files.push(rel);
    }
  }
  return files;
};

const titleFromPath = (path) => {
  const name = path.split('/').pop()?.replace('.md', '') ?? path;
  return name.replace(/-/g, ' ');
};

const groupFromPath = (path) => {
  if (path.startsWith('notes/')) return 'notes';
  if (path.startsWith('index/')) return 'index';
  return 'root';
};

const parseFrontmatter = (text) => {
  const match = text.match(/^---\n([\s\S]*?)\n---/);
  if (!match) return { title: null, tags: [] };

  const body = match[1];
  const lines = body.split('\n');
  let title = null;
  let tags = [];
  let inTagsList = false;

  for (const raw of lines) {
    const line = raw.trim();
    if (!line) continue;

    if (line.startsWith('title:')) {
      title = line.replace('title:', '').trim();
      continue;
    }

    if (line.startsWith('tags:')) {
      const rest = line.replace('tags:', '').trim();
      if (rest.startsWith('[') && rest.endsWith(']')) {
        tags = rest
          .slice(1, -1)
          .split(',')
          .map((tag) => tag.trim())
          .filter(Boolean);
        inTagsList = false;
      } else if (!rest) {
        inTagsList = true;
      }
      continue;
    }

    if (inTagsList) {
      if (line.startsWith('- ')) {
        tags.push(line.replace('- ', '').trim());
      } else {
        inTagsList = false;
      }
    }
  }

  return { title, tags };
};

const main = async () => {
  const files = await walk(contentRoot);
  const manifest = [];

  for (const path of files) {
    const raw = await readFile(join(contentRoot, path), 'utf-8');
    const fm = parseFrontmatter(raw);
    manifest.push({
      path,
      title: fm.title || titleFromPath(path),
      tags: fm.tags || [],
      group: groupFromPath(path)
    });
  }

  await writeFile(outputPath, JSON.stringify(manifest, null, 2));
};

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
