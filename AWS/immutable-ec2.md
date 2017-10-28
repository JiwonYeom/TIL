## EC2 as an Immutable Infrastructure

이 문서는 AWSKRUG에서 정도현님의 발표를 듣고 난 후 정리한 것입니다.

- In modern architecture, deploying means deploying environment not deploying an app. It is analoguous to deploying a data center.

- Every deployment requires automated testing + code review

- Conventionallly, EC2s are continously updated.

- In this approach, EC2s are not updated. They are re-created. Taking the term *instance* as a literal meaning.

- Bake configs, data, status into AMI. Do real-time back up of logs & preserve cache through S3, dynamoDB, ElastiCache, etc.

- Save multiple EC2s into different regions.

##### Modern infrastructure
- fault tolerance
- extensibility
- redundancy
- eventual consistency
- storage service
- stateless