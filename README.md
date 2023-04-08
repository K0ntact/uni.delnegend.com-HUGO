# Notes
- Theme: [Geekdocs](https://geekdocs.de/)
- Types of hint: note, tip, important, caution, warning

# Development
## Requirements
- [Hugo extended](https://github.com/gohugoio/hugo/releases)
- [Python](https://www.python.org/downloads/)
- `libavif` (avifenc only, optional) and `ffmpeg`
  - jeremylee.sh/bins: [avifenc](https://jeremylee.sh/bins/avif.7z), [ffmpeg](https://jeremylee.sh/bins/ffmpeg.7z)
  - [libavif](https://github.com/AOMediaCodec/libavif)
  - [ffmpeg](https://ffmpeg.org/download.html)
## Local server
```bash
hugo server
```
- add '-D' to include drafts
- add '--disableFastRender' to fully render

## Build
Just push

## New post
- Folder structure: `content/<subject>/<post>/index.md`\
**DO NOT USE SPACE IN FOLDER NAME OR FILE NAME**
- Front matter
  ```yaml
  ---
  title: "Title"
  draft: false
  ---

  {{<toc>}}
  ```

# Insert image
```markdown
![](image_name.webp)
```
- Throw the original image into the same folder as the post, extension must be `.png`
- Run `python OPTIMIZE.py` to optimize the image (convert to `webp` and `avif`)