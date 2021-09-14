Title: Gin API 示例 【进行中】
Date: 2021-09-14 22:20
Slug: gin-api-examples
Category: Post
Tags: Golang, Go
Status: published

## 1. AsciiJSON

使用 AsciiJSON 生成纯 ASCII JSON, 非 ASCII 字符会被转义。

```go
func main() {
	r := gin.Default()

	r.GET("/someJSON", func(c *gin.Context) {
		data := map[string]interface{}{
			"lang": "GO语言",
			"tag":  "<br",
		}
		// 将会输出 : {"lang":"GO\u8bed\u8a00","tag":"\u003cbr"}
		c.AsciiJSON(http.StatusOK, data)
	})

	// 在 0.0.0.0:8080 上监听
	r.Run(":8080")
}
```

测试：
```bash
$ curl http://localhost:8080/someJSON

{"lang":"GO\u8bed\u8a00","tag":"\u003cbr"}
```

注意，如果使用chrome浏览器访问这个地址，浏览器中会显示，这是浏览器自动进行了处理：
```json
{
  lang: "GO语言",
  tag: "<br"
}
```


## 2. 绑定表单请求数据到自定义的 struct

下列示例使用了自定义的`struct`:

```go
type StructA struct {
    FieldA string `form:"field_a"`
}

type StructB struct {
    NestedStruct StructA
    FieldB string `form:"field_b"`
}

type StructC struct {
    NestedStructPointer *StructA
    FieldC string `form:"field_c"`
}

type StructD struct {
    NestedAnonyStruct struct {
        FieldX string `form:"field_x"`
    }
    FieldD string `form:"field_d"`
}

func GetDataB(c *gin.Context) {
    var b StructB
    c.Bind(&b)
    c.JSON(200, gin.H{
        "a": b.NestedStruct,
        "b": b.FieldB,
    })
}

func GetDataC(c *gin.Context) {
    var b StructC
    c.Bind(&b)
    c.JSON(200, gin.H{
        "a": b.NestedStructPointer,
        "c": b.FieldC,
    })
}

func GetDataD(c *gin.Context) {
    var b StructD
    c.Bind(&b)
    c.JSON(200, gin.H{
        "x": b.NestedAnonyStruct,
        "d": b.FieldD,
    })
}

func main() {
    r := gin.Default()
    r.GET("/getb", GetDataB)
    r.GET("/getc", GetDataC)
    r.GET("/getd", GetDataD)

	r.POST("/getb", GetDataB)
	r.POST("/getc", GetDataC)
	r.POST("/getd", GetDataD)

    r.Run()
}
```
使用 `curl` 命令测试：

```bash
# 下面3个命令使用query string 传递数据
$ curl "http://localhost:8080/getb?field_a=hello&field_b=world"
{"a":{"FieldA":"hello"},"b":"world"}

$ curl "http://localhost:8080/getc?field_a=hello&field_c=world"
{"a":{"FieldA":"hello"},"c":"world"}

$ curl "http://localhost:8080/getd?field_x=hello&field_d=world"
{"d":"world","x":{"FieldX":"hello"}}

# 下面3个命令使用表单传递数据
$ curl -X POST -d "field_a=hello&field_b=world" "http://localhost:8080/getb"
{"a":{"FieldA":"hello"},"b":"world"}

$ curl -X POST -d "field_a=hello&field_c=world" "http://localhost:8080/getc"
{"a":{"FieldA":"hello"},"c":"world"}

$ curl -X POST -d "field_x=hello&field_d=world" "http://localhost:8080/getd"
{"d":"world","x":{"FieldX":"hello"}}

```

从测试可以看出，上面的方法不但可以绑定来自`query string`的数据，还可以绑定来自表单的数据

## 3. Bind html checkboxes

main.go

```go
...

type myForm struct {
    Colors []string `form:"colors[]"`
}

...

func formHandler(c *gin.Context) {
    var fakeForm myForm
    c.ShouldBind(&fakeForm)
    c.JSON(200, gin.H{"color": fakeForm.Colors})
}

...
```

form.html

```html
<form action="/" method="POST">
    <p>Check some colors</p>
    <label for="red">Red</label>
    <input type="checkbox" name="colors[]" value="red" id="red">
    <label for="green">Green</label>
    <input type="checkbox" name="colors[]" value="green" id="green">
    <label for="blue">Blue</label>
    <input type="checkbox" name="colors[]" value="blue" id="blue">
    <input type="submit">
</form>
```
result:
```javascript
{"color":["red","green","blue"]}
```

## Bind query string or post data

```go
package main

import (
	"log"
	"time"

	"github.com/gin-gonic/gin"
)

type Person struct {
	Name     string    `form:"name"`
	Address  string    `form:"address"`
	Birthday time.Time `form:"birthday" time_format:"2006-01-02" time_utc:"1"`
}

func main() {
	route := gin.Default()
	route.GET("/testing", startPage)
	route.Run(":8085")
}

func startPage(c *gin.Context) {
	var person Person
	// If `GET`, only `Form` binding engine (`query`) used.
	// If `POST`, first checks the `content-type` for `JSON` or `XML`, then uses `Form` (`form-data`).
	// See more at https://github.com/gin-gonic/gin/blob/master/binding/binding.go#L48
	if c.ShouldBind(&person) == nil {
		log.Println(person.Name)
		log.Println(person.Address)
		log.Println(person.Birthday)
	}

	c.String(200, "Success")
}
```

Test it with:

```bash
$ curl -X GET "localhost:8085/testing?name=appleboy&address=xyz&birthday=1992-03-15"
```

## Bind Uri

```go
package main

import "github.com/gin-gonic/gin"

type Person struct {
	ID   string `uri:"id" binding:"required,uuid"`
	Name string `uri:"name" binding:"required"`
}

func main() {
	route := gin.Default()
	route.GET("/:name/:id", func(c *gin.Context) {
		var person Person
		if err := c.ShouldBindUri(&person); err != nil {
			c.JSON(400, gin.H{"msg": err})
			return
		}
		c.JSON(200, gin.H{"name": person.Name, "uuid": person.ID})
	})
	route.Run(":8088")
}
```

Test it with:

```bash
$ curl -v localhost:8088/thinkerou/987fbc97-4bed-5078-9f07-9141ba07c9f3
$ curl -v localhost:8088/thinkerou/not-uuid
```

## Build a single binary with templates

### Use the third-party package

You can use the third party package to build a server into a single binary containing templates by using go-assets.

```go
func main() {
	r := gin.New()

	t, err := loadTemplate()
	if err != nil {
		panic(err)
	}
	r.SetHTMLTemplate(t)

	r.GET("/", func(c *gin.Context) {
		c.HTML(http.StatusOK, "/html/index.tmpl", nil)
	})
	r.Run(":8080")
}

// loadTemplate loads templates embedded by go-assets-builder
func loadTemplate() (*template.Template, error) {
	t := template.New("")
	for name, file := range Assets.Files {
		if file.IsDir() || !strings.HasSuffix(name, ".tmpl") {
			continue
		}
		h, err := ioutil.ReadAll(file)
		if err != nil {
			return nil, err
		}
		t, err = t.New(name).Parse(string(h))
		if err != nil {
			return nil, err
		}
	}
	return t, nil
}
```
See a complete example in the assets-in-binary/example01 directory.

未完待续......