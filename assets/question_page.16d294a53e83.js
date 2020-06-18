var json_object;
var question_number=0;
var result=0;
async function retrieve_data_from_backend()
{
    document.getElementById("A").style.backgroundColor="black";
    document.getElementById("B").style.backgroundColor="black";
    document.getElementById("C").style.backgroundColor="black";
    document.getElementById("D").style.backgroundColor="black";
    document.getElementById("result_part").style.display="None";
    document.getElementById("A").style.color="white";
    document.getElementById("B").style.color="white";
    document.getElementById("C").style.color="white";
    document.getElementById("D").style.color="white";
    document.getElementById("result_part").style.display="None";
    let response=await fetch("http://127.0.0.1:8000/quiz_page/");
    if(response.ok)
    {
        let json_data=await response.json();
        console.log("The data is",json_data);
        this.json_object=JSON.parse(json_data)
        console.log("The json_object",this.json_object)
    }
    document.getElementById("question_got").innerHTML=this.json_object[0].fields.question;
    document.getElementById("A").innerHTML=this.json_object[this.question_number].fields.option1;
    document.getElementById("B").innerHTML=this.json_object[this.question_number].fields.option2;
    document.getElementById("C").innerHTML=this.json_object[this.question_number].fields.option3;
    document.getElementById("D").innerHTML=this.json_object[this.question_number].fields.option4;
    //this.question_number=this.question_number+1;
    console.log("Hii",response)
}
function change_next_question()
{
    document.getElementById("A").disabled=false;
    document.getElementById("B").disabled=false;
    document.getElementById("C").disabled=false;
    document.getElementById("D").disabled=false;
    document.getElementById("A").style.backgroundColor="black";
    document.getElementById("B").style.backgroundColor="black";
    document.getElementById("C").style.backgroundColor="black";
    document.getElementById("D").style.backgroundColor="black";
    document.getElementById("result_part").style.display="None";
    document.getElementById("A").style.color="white";
    document.getElementById("B").style.color="white";
    document.getElementById("C").style.color="white";
    document.getElementById("D").style.color="white";
    this.question_number=this.question_number+1;
    if(this.question_number>4)
    {
        console.log("Hii I am here");
        document.getElementById("question_answer_part").style.display="None";
        document.getElementById("result_part").style.display="Block";
    }
    else
    {
        document.getElementById("question_got").innerHTML=this.json_object[this.question_number].fields.question;
        document.getElementById("A").innerHTML=this.json_object[this.question_number].fields.option1;
        document.getElementById("B").innerHTML=this.json_object[this.question_number].fields.option2;
        document.getElementById("C").innerHTML=this.json_object[this.question_number].fields.option3;
        document.getElementById("D").innerHTML=this.json_object[this.question_number].fields.option4;
        //this.question_number=this.question_number+1;
    }
}
function check_result(option_choosed)
{
    console.log("The option chosed is ",option_choosed)
    console.log("Hey",this.json_object[this.question_number].fields.correct_answer)
      if(option_choosed==this.json_object[this.question_number].fields.correct_answer)
      {
            console.log("I am here");
            this.result=this.result+1;
            document.getElementById(option_choosed).style.backgroundColor="green";
      }
      else
      {
            document.getElementById(option_choosed).style.backgroundColor="red";
            document.getElementById(this.json_object[this.question_number].fields.correct_answer).style.backgroundColor="green";
      }
      document.getElementById("A").disabled=true;
      document.getElementById("B").disabled=true;
      document.getElementById("C").disabled=true;
      document.getElementById("D").disabled=true;
      //change_next_question();
      document.getElementById("result").innerHTML=this.result;
}