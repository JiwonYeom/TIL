## Code review tips

#### What to do 
- If need to clarify some parts, make extra comments after committing
- If some parts are to be left as `TODO`'s, mention them clearly within the comments. 
- If close to release/end of sprint, compromise on code styles instead of trying to refactor everything. (Make sure to come back at these later)

#### Lessons learnt
- Instead of using `magic numbers`, define them as constants.
- For most cases, make extra logics(that are not part of original) into separate methods
- For methods that will not be used outside class, define them as private
- For constants that will not be used outside class, define them as private
- IN short, define `Access Modifiers` Accordingly
- Use `DOC`s at correct times, appropriately ==> Right definitions of DOcs will induce IDE to generate functions/indicators
- Use proper data type definitions
- 역할에 알맞는 코드와 객체, 함수 등을 이용하도록 하자.
- Write codes that can be understood WITHOUT additional knoweldge (follow the natural flow)
- `return` early insteand of `if..else` if possible.
- Actively use `constructors` in case of request/response models
- Sometimes verbose code is better than overly abbreviated codes. Make it logical & followable by others.