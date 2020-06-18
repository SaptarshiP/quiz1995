from login.views import retrieve_login_credential
from .models import question_bank
class question_manipulation:
    def retrieve_the_applicant_roll_number(self):
        #retrieve_login_credential()
        return retrieve_login_credential.applicant_roll_number
    def retrieve_all_the_question(self):
        data_retrieve_database=[]
        roll_number=self.retrieve_the_applicant_roll_number()
        temp = roll_number
        print("temp",temp)
        count = 0
        while temp>0:
            count = count+1
            print("inside count,temp",count,temp)
            temp,decimal = divmod(temp,10)
        obj=question_manipulation()
        starter=obj.recur2(roll_number)
        if count > 5:
            count = 5
        print("data_got",starter)
        print("count",count)
        i=1
        while i<=10:
            data_retrieve = question_bank.objects.filter(question_number=starter)
            print("data_retrive",data_retrieve[0].question)
            data_retrieve_database.append(data_retrieve[0])
            starter=starter+count
            i = i+1
        print("data_retrieve",data_retrieve_database[0].question)
        return data_retrieve_database
    def recur2(self,roll_number):
        obj=question_manipulation()
        if roll_number<10:
            print("Hii I am here",roll_number)
            return roll_number
        temp=roll_number
        sum=0
        while temp>0:
            g,h=divmod(temp,10)
            sum=sum+h
            temp,h1=divmod(temp,10)
            print("sum,temp,h,h1",sum,temp,h,h1)
        return obj.recur2(sum)
