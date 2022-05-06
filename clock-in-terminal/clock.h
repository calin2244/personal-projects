#if !defined(CLOCK_H)
#define CLOCK_H

#include <string>  

namespace date_independent {

    namespace clock{

        class at{
            int hour, minute;
            public:

                at() = default;

                at(int hr, int min){
                    
                    if(min >= 0){
                        minute = min % 60;
                        hr += min / 60;
                    }
                    else{
                        minute = 60 - ((min * -1) % 60);
                        hr -= ((min * -1) / 60) + 1;
                    }

                    if(hr >= 0)
                        hour = hr % 24;
                    else
                        hour = 23 - ((hr * -1 -1) % 24);
                }

                int getMinutes() const{
                    return minute;
                }

                int getHour() const{
                    return hour;
                }

            at plus(int plusMins){
                return at(hour, minute + plusMins);
            }

            operator std::string() const{
                std::string current_hour;
                if(hour == 24 || hour == 0)
                    current_hour += "00";
                else if(hour < 10)
                    current_hour += "0" + std::to_string(hour);
                else current_hour += std::to_string(hour);

                if(minute < 10)
                    current_hour += ":0" + std::to_string(minute);
                else current_hour += ":" + std::to_string(minute);

                return current_hour;
            }

            /* Comparing the hour and minute of the current clock to the hour and minute of the clock passed in. 
               Not necessary for the clock to work, used for testing purposes. */
            bool operator==(const at clock2){
                return this->hour == clock2.hour && this->minute == clock2.minute ? true : false;
            }

        };
    }
}  // namespace date_independent

#endif // CLOCK_H
