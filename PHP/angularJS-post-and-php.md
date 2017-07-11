# AngularJS(1.x) HTTP post method & PHP
* What happened?

I was working on my company's web application (`CI3`) and so far while I was using `jQuery` Ajax, I had no problem with CI method of getting `POST` inputs. I used the following code.

```
$date = $this->input->post('date');
```
This worked well in both `GET` and `POST` methods and there was no need for me to adjust anything extra. So I did the same thing with `AngularJS` HTTP methods.

```
//js script
var company = $('.selectwrap.company a').text();
var date = $('.selectwrap.date a').text();
var postData = {
    company : company,
    date : date
};
$http.post("url", postData).then(
    function(response) {
        console.log(response);
    },
    function(error){
        console.log(error);
    });

// php
...
$date = $this->input->post('date');
```

And it turned out the post input was empty. I tried to go around it but I was without success, and after doing some search I found that `AngularJS`, unlike `jQuery`, sets **Content-Type** header into `application/json` instead of `application/x-www-form-urlencoded`, which is what `jQuery` uses.

In order to read this value properly, `PHP` should read it from raw input. So I wrote this:

```
$postdata = file_get_contents("php://input");
$postdata = json_decode($postdata);
$date = $postdata->date;
$company = $postdata->company;
```
And it worked. Apparently the `header` setting for different library - or framework - matters!
