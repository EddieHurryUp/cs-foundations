import { readdir, stat, writeFile } from 'node:fs/promises';
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

const main = async () => {
  const files = await walk(contentRoot);
  const manifest = files.map((path) => ({
    path,
    title: titleFromPath(path),
    group: groupFromPath(path)
  }));
  await writeFile(outputPath, JSON.stringify(manifest, null, 2));
};

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
