module.exports = function (eleventyConfig) {
  // Return your Object options:
  eleventyConfig.addLayoutAlias('default', 'index.njk')
  eleventyConfig.addPassthroughCopy("assets");
  eleventyConfig.addPassthroughCopy("old/images");
  eleventyConfig.addPassthroughCopy({ "old/images": "images" });
  const pluginTOC = require('eleventy-plugin-nesting-toc');
  eleventyConfig.addPlugin(pluginTOC);
  const markdownIt = require('markdown-it');
  const markdownItAnchor = require('markdown-it-anchor');
  eleventyConfig.setLibrary("md",
    markdownIt({
      html: true,
      linkify: true,
      typographer: true,
    }).use(markdownItAnchor, {})
  );
  return {
    markdownTemplateEngine: 'njk',
    dataTemplateEngine: 'njk',
    htmlTemplateEngine: 'njk',

    dir: {
      input: ".",
      output: "html"
    }
  }
};