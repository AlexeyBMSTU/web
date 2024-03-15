// #include <iostream>
// #include <cassert>

// //template<class T>
// class Queue {
// public: 
//     Queue();   //Constructor
//     ~Queue();  //Destructor

//     Queue( Queue& ) = delete;
//     Queue& operator=(const Queue& ) = delete;

//     void Enqueue( int data );
//     int Dequeue();
//     int Size() const;


// private:
// struct Node 
// {
//     int Data;
//     Node* Next;
//     Node() : Data ( 0 ), Next ( nullptr ) {}
// };

// Node *head;
// Node* tail;
// int size;

// };

// Queue::Queue() : head( nullptr ), tail( nullptr ), size( 0 ) {  //Constructor

// }   

//   Queue::~Queue(){
//     while( head != nullptr){
//         Node* nextNode = head->Next;
//         delete head;
//         head = nextNode;
//     }

//   }  //Destructor

// void Queue::Enqueue( int data ){   //Добавить в очередь

//     Node* newNode = new Node;
//     newNode->Data = data;
//     if ( size == 0 ) {
//         tail = head = newNode;
//     } else{

//         tail->Next = newNode;
//         tail = newNode;
//     }
//     ++size;

// }
// int Queue::Dequeue(){      //Убрать с очереди

//     assert( size > 0 );

//     int returnData = head->Data;
//     Node* nodeToDelete = head;
//     head = head->Next;
//     delete nodeToDelete;
//     --size;
//     if (size == 0){
//         assert(head == nullptr);
//         tail = nullptr;
//     }
//     return returnData;
// }

// int Queue::Size() const{
//     return size;
// }




// int main(){

//     int* arr = new int[1000];
//     delete[] arr;
//     Queue intQueue;
//     intQueue.Enqueue( 123 );
//     std:: cout << intQueue.Dequeue() << std::endl;
//     //Queue intQueue;
//     int n = 0;
//     std::cin >> n;
//     bool result = true;

//     for (int i = 0; i<n; ++i){
//         int command = 0;
//         int data = 0;
//         std::cin >> command >> data;
//         switch(command) {
//             case 2:
//                 if (intQueue.Size() > 0){
//                     result = result && intQueue.Dequeue() == data;
//                 } else {
//                     result = result && data == -1;

//                 }
//                 break;
//             case 3:
//             intQueue.Enqueue( data );
//                 break;
//             default:
//                 assert(false);
//         }

//     }
//     std::cout << (result ? "YES" : "NO" )<< std::endl;
//      return 0;
// }



// #include <iostream>
// #include <stack>

// class Queue {
// private:
//     std::stack<int> pushStack;
//     std::stack<int> popStack;

// public:
//     void push(int value) {
//         pushStack.push(value);
//     }

//     int pop() {
//         if (popStack.empty()) {
//             while (!pushStack.empty()) {
//                 popStack.push(pushStack.top());
//                 pushStack.pop();
//             }
//         }

//         int value = popStack.top();
//         popStack.pop();
//         return value;
//     }

//     bool isEmpty() {
//         return pushStack.empty() && popStack.empty();
//     }
// };

// int main() {
//     Queue q;

//     q.push(1);
//     q.push(2);
//     q.push(3);

//     std::cout << q.pop() << "1 "<< std::endl;
//     std::cout << q.pop() << "2"<<  std::endl;

//     q.push(4);

//     std::cout << q.pop() <<"3"<< std::endl;
//     std::cout << q.pop() << "4"<<std::endl;

//     return 0;
// }


// class Stack{
// public:
//    explicit Stack( int _bufferSize );
//     ~Stack();

//     //Добавление и извлечение э-та из стека
//     void Push( int a );
//     int Pop();

//     //Проверка на пустоту
//     bool IsEmpty() const {
//         return top == -1;
//     }
//     int size();
// private:
//     int* buffer;
//     int bufferSize;
//     int top;
// };

// Stack::Stack( int _bufferSize ):
//     bufferSize( _bufferSize ),
//     top( -1 )
// {
//     buffer = new int[bufferSize]; //Создание буфера
// }
// Stack::~Stack(){
//     delete[] buffer;
// }

// void Stack::Push( int a ){
//     assert( top + 1 < bufferSize );
//     buffer[++top] = a;
// }
// int Stack::Pop(){
//     assert( top != -1);
//     return buffer[bufferSize - top];
// }

// int Stack::size(){
//     return top + 1;
// }
/*Реализовать очередь с помощью двух стеков. Использовать стек, реализованный с помощью динамического буфера.

Обрабатывать команды push back и pop front.

Формат ввода
В первой строке количество команд n. n ≤ 1000000.

Каждая команда задаётся как 2 целых числа: a b.

a = 2 - pop front
a = 3 - push back

Если дана команда pop front, то число b - ожидаемое значение. Если команда pop front вызвана для пустой структуры данных, то ожидается “-1”.

Формат вывода
Требуется напечатать YES - если все ожидаемые значения совпали. Иначе, если хотя бы одно ожидание не оправдалось, то напечатать NO.
*/
#include <iostream>
#include <cassert>
#include <sstream>
using namespace std;

class Push {
public:
    explicit Push(int _bufferSize);
    ~Push();

    //Добавление эл-та
    void Add( int a );
    int Del();
     Push( Push& ) = delete;
     Push& operator=(const Push& ) = delete;

    //Проверка на пустоту
    bool IsEmpty() const {
        return top == -1;
    }
    int size();
    int data(int data);

private:
    int *buffer;
    int bufferSize;
    int top;
};
class Pop {
public:
    explicit Pop(int _bufferSize);
    ~Pop();

    //Добавление эл-та
    void Add( int a );
    int Del();
     Pop( Pop& ) = delete;
     Pop& operator=(const Pop& ) = delete;
    
    //Проверка на пустоту
    bool IsEmpty() const {
        return top == -1;
    }
    int size();
    
private:
    int *buffer;
    int bufferSize;
    int top;
};


Push::Push( int _bufferSize ):
    bufferSize(_bufferSize),
    top(-1)
    {
        buffer = new int[bufferSize];
    }
Push::~Push(){
    delete[] buffer;
}
int Push::data( int value){
 

    return value;
}
void Push::Add(int a){
    assert( top + 1 <= bufferSize);
    buffer[++top] = a;

}
int Push::Del(){
    assert( top!= -1);
    return buffer[top--];
}
int Push::size(){
    return top + 1;
}

Pop::Pop( int _bufferSize ):
    bufferSize(_bufferSize),
    top(-1)
    {
        buffer = new int[bufferSize];
    }
Pop::~Pop(){
    delete[] buffer;
}

void Pop::Add(int a){
    assert( top + 1 <= bufferSize);
    buffer[++top] = a;


}
int Pop::Del(){
    //assert( top!= -1);
    return buffer[top--];
}
int Pop::size(){
    return top + 1;
}


int main(){

    int* arr = new int[1000];

    int n = 0;
    cin >> n;
    if (n >=1000000 || n <=0 ){
        return -1;
    }
    Push push(1000000);
    Pop pop(1000000);
    bool result = false;
    int command = 0;
    int data = 0;
    int index = 0;
   // std::cout << po.IsEmpty();
    for( int i = 0; i < n; ++i){
        cin >> command >> arr[index];
        
        switch(command){
            case 3: {

                push.Add(arr[index]);
                //cout << arr[index];
                //cout << push.data();
                // if (pop.IsEmpty()){
                //     pop.Add(temp);
                //     result = true;+++++
                   
                // }
    ++index;
   // cout << index << endl;
    result = true;
                break;
            }

            case 2: {
                if (pop.IsEmpty() && push.IsEmpty()){
                    //result = false;
                    if (i + 1 == n){
                        return -1;
                    }
                    break;
                }
                else if (pop.IsEmpty() && !push.IsEmpty()){

                    while(!push.IsEmpty()){
                       pop.Add(push.Del());
                       
                     //  cout << arr[index - 1]<< std::endl;
                       //index--;
                    }
                    //result = true;
                    //cout << pop.Del() << endl;
                    //cout << pop.Del() << endl;
                    //cout << pop.Del() << endl;
                   // cout << arr[index] << endl;
                   // cout << arr[index] << endl;
                    //cout << arr[i] << endl;
                    //cout << push.Del();
                    int del = pop.Del();
                    //cout << del;
                    result = result && del== arr[index ];
                   // cout << arr[i] << endl;
                  //  cout << result << endl;
                    break;

                }


                else {
                    
                    result = result && pop.Del() == arr[index];
                    //index++;
                    break;
                }
                
                //else {
                  //  result = result && arr[i] == -1;
                   
                    //std::cout << l << std::endl;
                    
               // }

               // break;
            }
            default: {
                assert(false);
            //return -1;
            break;
            
                
            }

        }
    }
 
    delete[] arr;

        cout << (result ? "YES" : "NO" )<< std::endl;

return 0;
   
}
// void testStack(){
//     {
//         std::stringstream input;
//         std::stringstream output;
//         input << "3 3 44 3 50 2 44";
//         run( input, output);
//         assert(output.str() == "YES");

//     }
//         {
//         std::stringstream input;
//         std::stringstream output;
//         input << "2 3 44 2 66";
//         run( input, output);
//         assert(output.str() == "NO");

//     }
// }
// int main(){
//     run(std::cin, std::cout);
//     testStack();
//     return 0;

// }


















