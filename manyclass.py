# Author:ctwo b

provinces_list = ['广东']
city_list = ['深圳', '广州', '惠州', '东莞', '佛山']
county_list = [{'深圳': ['福田', '罗湖', '南山', '龙岗', '龙华', '保安']},
               {'广州': ['天河', '越秀', '萝岗']}]
count = 0
while count < 3:
    destination = input('where are you going?: ').strip()
    if destination in provinces_list:
        print(city_list)
        city = input('which city you want to go?:').strip()
        for line in county_list:
            if city in line:
                print(line.get(city))
    count += 1

