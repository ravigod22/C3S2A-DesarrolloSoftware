const app = require("./app");

const port = process.env.PORT || 3001;

app.listen(port,()=>{
    console.log("Server running on port: %i",3001);
});
