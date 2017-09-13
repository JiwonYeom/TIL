
(might be migrated to Medium page later)
For those of you who have absolutely NO IDEA about the website url - like I was (and still partially am) - This is a simple guide.

1. Urls are made out of `protocol` part and `resource name` part.

2. Domains are, as you could assume, unique. You should visit domain provider (there are tons out there), and purchase one after searching your wanted domain pattern.

3. When you access an website, actually 2 things happen 1) your agent(PC, mobile, tablet... whatever) ask for certain domain, 2)`DNS` responds to you with matching IP address.

This means, even though what you see in the address bar in your browser is familiar `http://www.something.com`, this is just something that YOU see, not what browser actually visits.

When we visit website, its always towards its IP, not the letters you see (domains).

(add explanation later)

in short: the web addresses you see and the actual thing that runs the website are COMPLETELY detached. They are just mapped by `DNS`.

4. What is `DNS` then? This is also called `name server`. As its name suggests, it stores your domain and corresponding IP. There are many, many name servers out there, and they are *hierarchical*. Some name servers are named [Root Servers](https://www.iana.org/domains/root/servers), and they handle massive network of name servers. By forming networks and hierarchy, your website address query will travel through the network until it gets back the right IP address.

5. So it makes sense if ALL the name servers that have your domain and host(the server that carries website contents - simple version of seeing it) dies, you won't be able to access that website with web address.
Also, if the IP address changes and web address does not match with that IP address anymore in the registered `DNS`, it won't be accessible anymore.

6. Things are easier if you think of the **name of website** and the **contents container** of the website as two separate thing.
