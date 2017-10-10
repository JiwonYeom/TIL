## Caching (Web)

Reference from Udacity caching videos (https://www.youtube.com/watch?v=n__c7xY1ZcI)

* Cache is a hash table

#### When do we cache?
- When computation is slow
- When computation will run multiple times
- When output is the same for a particular input
- When your hosting provider charges you for DB access(AWS!)

#### Caching occurs in multiple places
1. Browser (Local)
2. In network (CDN) : When origin server is located quite far, and thus fetching content takes longer.
By putting contents nearby, less transfer happens and users enjoy faster access.

- Caches periodically expire
- Cache checks back to the origin server for changes in content.

#### Caching Technique
- No caching : every page view is DB read.
- Naive caching : If cache empty, do DB read. Bugs exist (front page becomes stale)
- Clear cache
- Refresh cache : rare DB read, 1 DB read per submission to DB
- Update cache : 0 DB read. 0 DB read when submission
When something gets updated, update DB, do NOT re-read from DB, just update cache right away.

\*Simple users shouldn't touch database - only read from cache.

#### Precomputed Caching
https://www.youtube.com/watch?v=H9J5vl_Huio

#### Memcached
https://www.youtube.com/watch?v=1MAgt0bFdwM
