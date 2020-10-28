const mongoose=require("mongoose");
var url="mongodb+srv://abhishek190:Jamesss@007@cluster0.iidxh.mongodb.net/mydb?retryWrites=true&w=majority";
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