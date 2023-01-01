module.exports = function(eleventyConfig) {
    // Return your Object options:
    eleventyConfig.addLayoutAlias('default', 'index.njk')
    eleventyConfig.addPassthroughCopy("assets");
    eleventyConfig.addPassthroughCopy("mediawiki_conversion/cleaned_data/images");
    eleventyConfig.addPassthroughCopy({ "mediawiki_conversion/cleaned_data/images": "images" });
    return {
      markdownTemplateEngine: 'njk',
      dataTemplateEngine: 'njk',
      htmlTemplateEngine: 'njk',

      dir: {
        input: ".",
        output: "dist"
      }
    }
  };