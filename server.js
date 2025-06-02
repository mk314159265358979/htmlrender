var express = require('express');
var bodyParser = require('body-parser');
var users = require("./userDatabase");

var app = express();

// var parser = bodyParser.urlencoded();
var parser = bodyParser.json();

app.use(parser);

app.use(express.static('public'));

app.get('/users', function(req, res) {
    users.getUsers((err, data) => {
        console.log("data: ", data);
        res.end(JSON.stringify(data));
    });
})

app.get('/add_user', function(req, res) {
    console.log(req.body);
    users.addUser(req.query.last_name, req.query.first_name);
    res.end("User added");
})
app.get('/profile', function(req, res) {
    res.send(`
        <html>
            <head><title>Profil</title></head>
            <body>
                <h1>Marek Koprowski</h1>
            </body>
        </html>
    `);
});
app.get('/index', function(req, res) {
    res.send(`
        <!DOCTYPE html>
<html>
<body>
<form action="http://add_user" method="GET">
	First name : <input type="text" name = "first_name"> <br>
	Last name : <input type="text" name = "last_name"> <br>
	<input type="submit" value = "Submit">
	
</form>
</body>
</html>
    `);
});
 const PORT = process.env.PORT || 8080;
const listener = app.listen(PORT);
//const listener = app.listen(8080, 
	//() => console.log(`Listening on ${ listener.address().port }`));

