#include "clock.h"
#include <iostream>
#include <vector>
#include <ctime>
#include <cstring>
#include <thread>
#include <chrono>

//Time Cases to check if the clock was working properly

/**
 * AddMins is a type that has three members: hour, minute, and mins_to_add.
 * @property {int} hour - The hour of the time you want to add minutes to.
 * @property {int} minute - The minute of the hour.
 * @property {int} mins_to_add - The number of minutes to add to the time.
 * Only used for testing the clock class.
 */

struct addMins{
    int hour;
    int minute;
    int mins_to_add; /* or to substract. */
};

std::vector<addMins> t = {
    {10, 0, 3}, {6, 41, 0}, {0, 45, 40},
    {10, 0, 61}, {0, 45, 160}, {23, 59, 2},
    {5, 32, 1500}, {1, 1, 3500}, {10, 3, -3},
    {10, 3, -30}, {10, 3, -70}, {0, 3, -4},
    {0, 0, -160}, {6, 15, -160}, {5, 32, -1500},
    {2, 20, -3000}, {4, 33, 278}, {1, 19, -20}
};

/**
 * @brief Get the Current Hour object
 * 
 * @param myClock 
 */

void getCurrentHour(date_independent::clock::at& myClock){
    
    /* Getting the current time of the system and storing it in a char array. 
       It's easier and more convenient to split a char array than a string. */
    char _time[6];
    time_t now = time(nullptr);
    auto time_info = localtime(&now);
    strftime(_time, 6, "%H:%M", time_info);
    char* token = strtok(_time, ":");

    int hour = std::stoi(token);
    token = strtok(NULL," ");
    int minute = std::stoi(token);
    myClock = date_independent::clock::at(hour, minute);
}

int main(){
    
    using namespace std::chrono_literals;

    /* A quick  test for the clock.
        date_independent::clock::at myClock(0, 0), myClock2();
        std::cout<<"Clock 1 \n";
        std::cout<<myClock.getHour()<<" "<<myClock.getMinutes()<<'\n'<<"After adding minutes \n";
        myClock.plus(160);
        std::cout<<myClock.getHour()<<" "<<myClock.getMinutes()<<" "<<static_cast<std::string>(myClock);
        for(addMins a : t){
         std::string clock_time = static_cast<std::string>(date_independent::clock::at(a.hour, a.minute).plus(a.mins_to_add));
         std::cout<<clock_time<<'\n';
        }
    */
    
    date_independent::clock::at theClock(0, 0);
    /* Getting the current hour of the system and setting the clock to that hour. */
    getCurrentHour(theClock);

    /* Printing the current time of the system every minute. */
    while(true){
        std::cout<<static_cast<std::string>(theClock)<<'\n';
        std::this_thread::sleep_for(60s);
        theClock = theClock.plus(1);
    }
}
