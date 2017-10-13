# Short Lesson on 204 Response
Today it happened to me that between REST API and client, response body came back empty even if it was set from REST API server.

We spent good 1 hour trying to solve this, and it turned out it was because of `204` response status.

`204 status` means the request was accepted and processed well, but `no content` is returned. It is in the series of 2xx, which is basically an okay sign.

Funny thing was, the message set from REST API server (which returned the `204` response) was well received when tested on [Postman](https://www.getpostman.com/apps).

But when it was attempted with `curl`, body was empty.

In the end we changed `204` to `200` and solved the problem, but I came home and did some search to see why did this happened.

I'm still not entirely sure, but it seems like setting `content-type` might be another solution.

Anyways, it seems like the response status should never be taken lightly.
