Title: How to write Markdown
Date: 2016-01-15 10:20
Category: Post


## Basic

### Paragraphs

Paragraphs in Markdown are just one or more lines of consecutive text followed by one or more blank lines.

```
On July 2, an alien mothership entered Earth's orbit and deployed several dozen saucer-shaped "destroyer" spacecraft, each 15 miles (24 km) wide.

On July 3, the Black Knights, a squadron of Marine Corps F/A-18 Hornets, participated in an assault on a destroyer near the city of Los Angeles.
```

### Headings

You can create a heading by adding one or more `#` symbols before your heading text. The number of `#` you use will determine the size of the heading.

```
# The largest heading (an <h1> tag)
## The second largest heading (an <h2> tag)
...
###### The 6th largest heading (an <h6> tag)
```

### Blockquotes

```
In the words of Abraham Lincoln:
> Pardon my french
```

### Styling text

You can make text **bold** or *italic*

```
*This text will be italic*
**This text will be bold**
```

Both **bold** and *italic* can use either a `*` or an `_` around the text for styling. This allows yo to combine both bold and italic if needed.

```
**Everyone _must_ attend the meeting at 5 o'clock today**
```

# Lists

### Unordered lists

You can make an unordered list by preceding list items with either a `*` or a `-`

```
* Item
* Item
* Item

- Item
- Item
- Item
```

### Ordered lists

You can make an ordered list by preceding list items with a number

```
1. Item 1
2. Item 2
3. Item 3
```

### Nested lists

You can create nested lists by indenting list items by two spaces.

```
1. Item 1
  1. A corollary to the above item.
  2. Yet another point to consider.
2. Item 2
  * A corollary that does not need to be ordered.
    * This is indented four spaces, because it's two spaces further than the item above.
    * You might want to consider making a new list.
3. Item 3
```

## Code formating

### Inline formats

Use single backticks (`) to format text in a special monospace format. Everything within the backticks appear as-is, with no other special formatting.

```
Here's an idea: why don't we take `SuperiorProject` and turn it into `**Reasonable**Project`.
```

### Multiple lines

You can use triple backticks(```) to format text as its down distinct block


### Links

You can create an inline link by wrapping text in brackets(`[]`), and then wrapping the link in parentheses(`()`)

For example, to created a hyperlink to [www.danidai.com](http://www.danidai.com), with a link text that says, Visit DaniDai.com!, you'd write this in Markdown: `[Visit Danidai.com!](http://www.danidai.com)`.

## GitHub Flavored Markdown

GitHub uses "GitHub Flavored Markdown", or GFM, across GitHub -- in issues, comments, and pull requests. It differs from standard Markdown (SM) in a few significant ways, and adds some additinal functionality.

### Differences from traditional Markdown

#### Multiple underscores in words

Where Markdown transforms underscores (`_`) in to italics, GFM ignores underscores in words, like this:

> wow_great_stuff

> do_this_and_do_that_and_another_thing.

This allows code and names with multiple underscores to render properly. To emphasize a portion of a work, use asterisks(`*).

#### URL autolinking

GFM will autolink standard URLs, so if you want to link to a URL(instead of setting link text), you can simply enter the URL and it will be turned into a link to that URL.

```
http://example.com
```

becomes

http://example.com

#### Strikethrough

GFM adds syntax to create strikethrough text, which is missing from standard Markdown.

```
~~Mistaken text.~~
```

becomes

~~Mistaken text.~~

#### Fenced code blocks

Standard Markdown converts text with four spaces at the beginning of each line into a code block; GFM also supports fenced blocks. Just wrap your code in ``` (as shown below) and you won't need to indent it by four spaces. Note that although fenced code blocks don't have to be preceded by a blank line—unlike indented code blocks—we recommend placing a blank line before them to make the raw Markdown easier to read.

    Here's an example:

    ```
    function test() {
      console.log("notice the blank line before this function?");
    }
    ```

Keep in mind that, within lists, you must indent non-fenced code blocks eight spaces to render them properly.

#### Syntax highlighting

Code blocks can be taken a step further by adding syntax highlighting. In your fenced block, add an optional language identifier and we'll run it through syntax highlighting. For example, to syntax highlight Ruby code:

    ```ruby
    require 'redcarpet'
    markdown = Redcarpet.new("Hello World!")
    puts markdown.to_html
    ```
    
```ruby
require 'redcarpet'
markdown = Redcarpet.new("Hello World!")
puts markdown.to_html
```

GitHub use [Linguist](https://github.com/github/linguist) to perform language detection and syntax highlighting. You can find out which keywords are valid by perusing [the languages YAML file](https://github.com/github/linguist/blob/master/lib/linguist/languages.yml).



## References

1. https://help.github.com/articles/markdown-basics
2. https://help.github.com/articles/github-flavored-markdown/
3. https://help.github.com/articles/writing-on-github/