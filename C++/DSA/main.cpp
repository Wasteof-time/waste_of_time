#include <iostream>
#include <list>
#include <chrono>

#define LIMIT 10000

struct ListNode {
    size_t data;
    struct ListNode * next;

    ListNode(size_t _data = 0) {
        data = _data;
        next = nullptr;
    }
};



class List {
public:
    List() {
        pointer = nullptr;
        HEAD = pointer;
        END = pointer;
        size = 0;
    }

    void push_back(size_t data) {
        if (size == 0) {
            HEAD = new ListNode(data);
            pointer = HEAD;
            END = HEAD;
            size ++;
        }
        else {
            auto* temp =  new ListNode(data);
            END->next = temp;
            END = temp;
            size ++;
        }
    }

    void delete_node(size_t index ){
        auto * temp = HEAD;
        for (size_t i = 0 ; i < index ; i ++ ) {
            temp = temp->next;
        }
        auto * to_delete = temp->next;
        temp->next = to_delete->next;
        delete to_delete;
    }

private:
    struct ListNode * pointer;
    struct ListNode * HEAD;
    struct ListNode * END;

    size_t size;
};


int main() {

    std::list<size_t> std_list {};
    List my_list {};


    auto start = std::chrono::high_resolution_clock::now();

    for (size_t i = 0 ; i < LIMIT ; i ++) {
        std_list.push_back(10);
    }

    std::cout << "Time of finishing (std): " << std::chrono::high_resolution_clock::now() - start << std::endl;

    start = std::chrono::high_resolution_clock::now();

    for (size_t i = 0 ; i < LIMIT ; i ++) {
        my_list.push_back(10);
    }

    std::cout << "Time of finishing (my): " << std::chrono::high_resolution_clock::now() - start << std::endl;

}
