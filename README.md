# Scripts
> Better scripts lead to better life

## Tampermonkey
- [Install](https://tampermonkey.net/)

## Scripts
- **[clean_csdn](https://github.com/idejie/Scripts/raw/master/clean_csdn.js): 优化csdn**
  - 去广告
  - 自动展开
  - 移除无用信息
  - 宽度适配
  - 效果： 
  ![](https://ws3.sinaimg.cn/large/006tNbRwly1fxp1i8nbrij31hz0u0wrq.jpg)
  ![](https://ws3.sinaimg.cn/large/006tNbRwly1fxp1ilhhiwj31hp0u0n4q.jpg)
- **[fuck_ucas_net](https://github.com/idejie/Scripts/raw/master/fuck_ucas_net.js): UCAS上网脚本**
  - just one line :
   ```javascript
   checkForm=()=>true;
   ```
  - 失效（不过还有其他方法，暂不公布，需要的联系）
-  UCAS Course Picker

    > 2019.1.9
    >
    > 2019.6.5 updated for summer-term

    ##### Environment

    - UCAS network

    - Python3 

    - `BeatifulSoup4` ,`requsets`   needed

      You can install them by `pip install BeatifulSoup4 requsets ` 

    ##### Config

    ```python
    username = "your_email@email.com"
    password = "your_password"
    courses = { 
        # "course_code":"dept_id"  
        # like:     "156560": "964"
    }
    ```

    ##### Run

    `python ucase_course_picker.py`

    ##### Tips

    - How to find `course_code` 

      - Login the http://sep.ucas.cn

      - Click ![](https://ws2.sinaimg.cn/small/006tNc79ly1fz0cu2yg0vj305q058jrq.jpg)

      - Select `school timetable`

        ![](https://ws1.sinaimg.cn/large/006tNc79ly1fz0cv6e83dj32fm0fcwj7.jpg)

      - Click an iterm's `course code`, the you can get the real `course_code`in address

        ![](https://ws2.sinaimg.cn/large/006tNc79ly1fz0cw0g32sj30u401i3yy.jpg)

    - How to find `dept_id`

      ![](https://ws1.sinaimg.cn/large/006tNc79ly1fz0d6n18kpj31fl0u04qq.jpg)
      
- A Tool for Shit SDU(Single Dogs University)


      **usge**


      1. environment
      ```
        python3+
      ```
      2. install `beautifulsoup`
      ```shell
        pip install beautifulsoup
      ```
      3. add your print, like
      ```python
        print(score_all)
       ```
       4. execute the py
       ```shell
          python3 tool4shitsdu.py
       ````
