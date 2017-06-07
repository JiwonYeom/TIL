# GET and POST in PHP curl - basics
## Basics
`curl` in PHP basically does the same thing as `curl` in different languages or environments, but `php` has its own way of using it. It is not too difficult though.
Here are basic codes I used when I was working on `GET` and `POST` request.

```
$ch = curl_init();
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);  // sets return value of executed curl transfer as a string instead of direct output

...

curl_exec($ch);
curl_close($ch);


```

* `curl_init()` : initialize your curl transfer
* `curl_setopt()` : curl_setopt() sets options for curl transfer
* `curl_exec()`: execute your curl transfer
* `curl_close()` : close (finish) curl transfer

### GET
```
$request_url .= '?' . http_build_query($fields);
```
in GET request, if you have parameters http_build_query() can help to build queries automatically.

### POST
```
curl_setopt($ch, CURLOPT_POST, TRUE); // set curl transfer type as post
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers); // set headers as needed
curl_setopt($ch, CURLOPT_POSTFIELDS, $fields); // set parameters

```
