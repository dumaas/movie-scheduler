Link shortener
- Take in long URLs, provide shorter URL response
- Never tell somebody no
- Don't store the same URL twice
- Scale
- Just post/get, no updates (user owned)

- DB schemas, what to index, REST spec
  - No frontend, auth, analytics, etc

## Requirements
- Take a long URL in, respond with a shorter URL
  - Shorter url should (by magic) work
- Fast, no duplicates

- Shorter URL is not user defined
- Both input / outputs should be unique

### Scale
- Total should exceed 1bn
- Low thousands

## Workflow
User types in URL -> hit our service -> return the working shorter URL

Link
- Original URL: str -> provided by the user
- Shortened URL: str -> will need to create -> index
- created: datetime
- last_accessed: datetime

key-value:
    longer_url: shorter_url

    shorter_url: longer_url

Client -> API Gateway -> Load Balancer -> LinkService -> Cache -> Postgres DB

Client -> Cache (get the longer_url) -> Postgres Read -> redirect or 404

Cache eviction should be Least Recently Used

How to shorten URLs?
- Unique, shorter (obviously), deterministic
- hash(url)[:50] -> deterministic
- uuid(url)[:50] -> not deterministic
- map to english characters ord("c") -> 4
  - a-z,A-Z,0-9,_,- (64)
  - 8 chars long -> 2.8 * 10^14

How to handle collisions?
- If detect collision, https://www.some-site.com/aklsdjfhaskldjhf
- alksjhask -> rehash

url = ""
shorten = hash(url)

link = # From the db
if link and link.url != url:
    shorten = hash(shorten)
