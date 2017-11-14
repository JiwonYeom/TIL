# Software Architecture
guide: https://www.udacity.com/course/software-development-process--ud805

- Software Architecture : set of principal design decisions about the system. 즉, 어떻게 명령을 내릴까에 대한 이야기.
- Blueprint of a software system
    - Structure
    - Behavior
    - Interaction
    - Non-functional properties
- Temporal Aspect: SWA is defined iteratively. SWA is bound to change. Design decisions keep on change as time goes

### Prescriptive
- design decisions made prior to the system's construction.
- as-conceived SWA

### Descriptive
- How the system has actually been built
- as-implemented SWA

### Architectural Evolution
- When a system evolves, prescriptive darchitecture gets modified -> descriptive architecture gets modified (설계를 먼저 수정한 후, 실제로 적용)
- But in SWA, that rarely happens. It happens the other way around
- why?
    - Developer's sloppiness
    - short deadlines
    - Lack of documented prescriptive architecture
    - ...
- Prescriptive & Descriptive architecture end up diverging.

### Architectural Degradation
- Architectural Drift : architectural design decisions that happen WITHOUT being incorporated in the prescriptive architecture.
    - What happens? : architecture becomes unnecessarily complex, incomprehensible, awkward.
- Architectural erosion : architecture design decision that violates prescriptive architecture.

### Architectural Recovery
- Drift and erosion might cause your architecture to degrade completely.
    1. Keep tweaking the code: Usually disastrous
    2. Architectural recovery: determine architecture from implementation and fix it from what was derived from it

### Software Architecture Elements <br>
Typically not a monolith.Composition and interplay of different elements
1. Processing elements
2. Data elementss
3. Interaction elements
> 1 and 2 are included in system components. <br>
> 3 is maintained and controlled by system connectors <br>
> Components and connectors together is configuration(topology)

### Deployment architectoral perspective
- Critical to access whether the system will satisfy the requirements. 
- Must consider all hardware characteristics (memory, network bandwidth, etc)

### Architectural Styles
- Pipes and Filters : Chain of processing elements (output of a process is input of another)
- Event-driven : Event emittors & consumers
- Publish-subscribe : publishers publish messages with limits to their audiences(subscribers) (ex.twitter)
- Client-Server : Server provides resources. Client consumes.
- Peer to Peer : Decentralized. Nodes become provider & consumer
- REST