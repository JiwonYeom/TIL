# [Codeigniter] How to use / make library
Recently I've been using Codeigniter, and here's how to use or create CI library.

## How to use it
CI default libraries are located in `system/libraries`, and in order to use it, you just need to initialize it and use it.

```
//initialize
$this->load->library('class-name');
```
Different library has different way to use it, so you need to check the [documentation](https://codeigniter.com/userguide3/libraries/index.html) for each library.

## How to create it
You can also create a library. According to CI documentation, we can do three things.
1. Create new library.
2. Extend native library.
3. Replace native library.
note* database class cannot be extended or replaced.

Keep three rules

1. Capitalize first letter for file names.
2. Capitalize first letter of class name.
3. Class name must match the file name.

After you create your library class, you can use it like when you are using native library.
But if you want to pass parameters when you initialize your class, you must make your constructor accept parameters.

```
class Someclass {

        public function __construct($params)
        {
                // Do something with $params
        }
}
```

Extending or utilizing CI resources in your library will be discussed in another time.
