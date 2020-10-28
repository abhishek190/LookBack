const mongoose=require("mongoose");
var url=process.env.MONGODB_URI
mongoose.connect(url,{ useNewUrlParser: true, useUnifiedTopology: true});
var db=mongoose.connection;

const UserDataSchema=new mongoose.Schema({
    email:String,
    title:String,
    timeLimit:String,
    memoryLimit:String,
    description:String,
    InputSpecification:String,
    OutputSpecification:String,
    rating:String,
    note:String
});

var user=module.exports=mongoose.model('UserData',UserDataSchema);
module.exports.StoreData=(newData,callback)=>{
    
    newData.save(callback)
}
