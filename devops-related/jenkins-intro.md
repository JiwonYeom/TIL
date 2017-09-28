## Introduction to Jenkins

> Keywords:
 Continuous Integration, Hudson

 * Installed on a central build server to let developers know the changed source code and trigger a build / run tests

 * Continuous Integration : a development practice that require developers to integrate code into shared repository at regular intervals. This is to prevent finding an issue AFTER problem has occurred. This means there must be frequent build cycle. Usually this means code commit->build.
 ([reference](https://www.tutorialspoint.com/jenkins/jenkins_overview.htm))

* Tutorials followed [here](https://www.tutorialspoint.com/jenkins/jenkins_maven_setup.htm)

* Core concepts
    - **Pipeline**: Supportive plugins for continuous delivery pipeline (automated flow of your version control -> users). Every change that is committed in source control goes through a complex process to be released.
    - Provides set of tools for modeling delivery pipelines "as code". )(Through Domain Specific Language syntax)
    - Continuous delivery pipeline is treated as a part of the application.
    - It's versioned & reviewed, just like other codes.
    - This text file is called `Jenkinsfile`

    > `Jenkinsfile`?
    > - Automatically create Pipelines for all Branches and Pull Requests.
    > - Code review/iteration on the Pipeline.
    > - Audit trail for Pipeline
    > - Single source of truth for Pipeline. Can be viewed & edited by many members.

    - Why do we need this?
        - Because the core concept of Jenkins is `Automation`. It is to provide full support from simple CI to comprehensive CI.

    - Pipeline Flow : refer to [this](https://jenkins.io/user-handbook.pdf) document figure 1.

    - Pipeline terms
        - **Step** : Single task. Command for Jenkins.
        - **Node** : Work that Pipeline performs. Nodes 1) schedules steps contained within the block to run by adding an item into the Jenkins `queue`. 2) Creates workspace which is a directory specific to that particular Pipeline.
        - **Stage** : Step for defining subset of the entire Pipeline. Ex) "Build", "Test", "Deploy"...
