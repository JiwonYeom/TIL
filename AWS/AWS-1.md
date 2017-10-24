#### Region / Availability Zone
사용자의 인스턴스들을 어느 지역의 서버 풀을 이용할것인지 정의할 수 있다. 각 지역(region)에는 여러개의 가용성 존(AZ)가 있으며, VPC 등을 여러개의 AZ에 걸쳐 설정하는 등으로 fault-tolerant한 서비스 설계가 가능하다

#### EC2
* EC2 instance: 말 그대로 서버 인스턴스. 생성시에 운영체제, 스펙 등을 조정해서 생성하고, AMI 라는 image 식으로 이미 본 떠져 있는 형태를 이용해서 생성할 수도 있다.

* Elastic Block Storage : 기본적으로 따라붙는 EC2 인스턴스의 저장소. 이것을 설정하지 않으면 인스턴스를 껐다 키면 모든 데이터가 날라간다.

* Elastic Load Balancer (ELB): 자동으로 여러대의 인스턴스에 부하를 분산해주는 인스턴스. 당연히도 인스턴스가 여러대여야 활용 가능하다.

* Auto-scaling: 각각의 EC2 인스턴스의 부하(load) 정도가 지정된 수준보다 높거나 낮을 때 알아서 인스턴스를 증설 / 감설하는 서비스.

#### RDS
* AWS 상에서 제공되는 Database. MySQL, PostgreSQL, Oracle 등등 Aurora라는 자체 DB도 제공한다.
* Security Group 을 세팅할때는 MySQL용 규칙을 별도로 추가해 주어야 한다

#### S3
* 정적인 데이터를 저장하는 저장소. 필요에 따라 다른 plan을 선택해서 과금 정도를 최적화 할 수 있다.
설정에 따라 정적인 사이트를 호스팅 할 수도 있어서 EC2 없이 사이트를 운영할 수도 있다.

#### CodeDeploy
* 자동으로 배포될 파일들의 변화를 감지, 재배포해주는 서비스.
