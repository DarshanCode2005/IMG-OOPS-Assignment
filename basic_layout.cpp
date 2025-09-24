#include <iostream>
#include <vector>
#include <string>
using namespace std;
bool exists(string s){

}
void signUp(){
    string id;
    cout<<"Enter ID"<<endl;
    cin>>id;
    if(exists(id)){
        cout<<"The ID is already registered. Kindly login to continue"<<endl;
        login();
    }
    else{
        cout<<"Enter name"<<endl;
        string name;
        cin>>name;
        cout<<"Create Password"<<endl;
        students.push_back(new student(id,name,password));
        cout<<"Registered Successfully"<<endl;
        login();
    }
}
void login(){
    string id;
    cout<<"Enter ID"<<endl;
    cin>>id;
    string password;
    cout<<"Enter password"<<endl;
    cin>>password;
    for(auto s : students){
        if(s->login(id,password)){
            logginInUser=s;
            cout<<"Login Successful! Welcome"<<s->getName()<<endl;
            return;
        }
        cout<<"Invalid Login ID or password"<<endl;
    }
};
int main(){
    cout<<"Welcome To The Club Management Portal"<<endl;
    cout<<"Press the number to execute"<<endl;
    cout<<"1. Sign Up"<<endl;
    cout<<"2. Log In"<<endl;
    int n;
    cin>>n;
    if(n==1){
        signUp();
    }
    else if(n==2){
        login();
    }
}