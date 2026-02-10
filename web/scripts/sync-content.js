import { cp, mkdir, rm } from 'node:fs/promises';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const root = join(__dirname, '..', '..');
const target = join(__dirname, '..', 'public', 'content');

const copyDir = async (src, dest) => {
  await rm(dest, { recursive: true, force: true });
  await mkdir(dest, { recursive: true });
  await cp(src, dest, { recursive: true });
};

const main = async () => {
  await mkdir(target, { recursive: true });
  await copyDir(join(root, 'notes'), join(target, 'notes'));
  await copyDir(join(root, 'index'), join(target, 'index'));
  await cp(join(root, 'README.md'), join(target, 'README.md'));
};

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
