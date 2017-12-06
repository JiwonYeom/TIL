ref: Computer Organization and Design By Patterson Hennessy

* Servers: Modern form of once much larger computers. Usually accessed only via network. They usually carry large workload. 
* Embedded Computers: largest class of computers.
    * widest range of applications & performance

* Warehouse Scale Computers(WSC): giant datacenters foro cloud computing

#### 8 Great ideas in computer architecture
* Moore's Law: integrated circuit resources double every 18-24 months.
* Abstraction for simplified design
* Make common case fast : enhances performance better than optimizing the rare case.. You will know what the common case is only through careful experimentation and measurement.
* performance via parallelism
* performance via pipelining
* performance via prediction
* hierarchy of memories
* Dependability via redundancy

#### Below your program
* OS
    * Handle basic input & output
    * allocate storage & memory
    * provide protected sharing of the computer among multiple applications, using them simultaneously.
* Compiler: translation of high-level language programs to the language that hardware can execute.

#### High-Level language & language of Hardware
* Instructions are collections of bits that computer understands.
* assembler: program that translates symbolic version of instructions into the binary
* assembly language: symbolic representation of machine instructions. This language requires programmer to write one line for every instruction. This forces programmer to think like computer.
* machine language: binary representation of machine instruction

> Relationship between program and languages
> high-level language ==> compiler ==> Assembly language ==> Assembler ==> Binary machine language

#### Under the Covers
> Classic component of a computer : input, output, memory, datapath, and control. (Datapath & Control often combined and called the processor)

##### Through the looking glass
* Liquid Crystal Displays(LCDs) : thin layer of liquid polymers that can be used to transmit / block light according to the charge applied.
* active matrix display: liquid crystal display using a transistor to control transmission of light at each individual pixel. 

##### Opening the box
* integrated circuit: also called a chip. Device combining dozens to millions of transistors.
* datapath: component of the processor (performs arithmetic operations)