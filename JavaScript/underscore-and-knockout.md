# Underscore.JS and KnockOut.JS
I've wrote an [article](https://jwyblog.wordpress.com/2017/05/21/choosing-a-template-engine/) in blog about how I am using / learning these two different template engines :)

Check it out! Here are codes that I whipped up quick for my posting.

```
<div>
  <ul id="nameList">
    <li>John Doe</li>
    <li>Jane Doe</li>
    <li>Mark Jakobs</li>
    <li>Sally Smith</li>
  </ul>
</div>

<script type="text/template" id="nameTmpl">
  _.each(nameList, function(name){
    <li><%= name%></li>
  });
</script>

<script>
  var data = ['Sirius Black', 'Remus Lupin', 'James Potter'];
  var nameHtml = $('#nameTmpl').html();
  $('#nameList').html(_.template(nameHtml,data));
 //$.ajax...
</script>
```

```
function myModel() {
  var self = this;
  self.names = ko.observableArray([]);

  $.getJSON("/api/getNames", function(data) {
    self.names(data);
  })
}

ko.applyBindings(new myModel());
```
