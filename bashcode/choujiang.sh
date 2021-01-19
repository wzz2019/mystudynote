#! /bin/bash
#用cat直接输出数据，空格会变成换行
rand1(){
    seeds=`cat a.txt`
    #echo "$seeds"
    for seed in $seeds;do
        echo $seed
    done
}
#去除空格语法：${line// /..}
rand2(){
    seeds=`while read line; do echo ${line// /..}; done <a.txt`
    for seed in $seeds;do
        echo $seed
    done
}
#缩小取数范围：随机取数
#每次取值行数都不固定
rand3(){
   local seeds=`while read line; do echo ${line// /..}; done <a.txt`
   seeds=`for seed in $seeds;do (( $RANDOM % 2 )) && echo $seed; done`
   echo "$seeds"
}

#继续缩小取数范围：只取1行数据
#此版本会出现结果为空的情况
rand4(){
   local seeds=`while read line; do echo ${line// /..}; done <a.txt`
   local count=0
   while [[ $count != 1 ]];do
        seeds=`for seed in $seeds;do (( $RANDOM % 2 )) && echo $seed; done`
        #echo "$seeds"
        #echo "$seeds"|wc -l
        count=`echo "$seeds"|wc -l`
   done
   #echo "$seeds"
   if [[ $seeds == "" ]];then
        rand4
   else
        echo "$seeds"
   fi
}

#每次抽1个，共抽10个，即原函数执行10次即可
#需要处理重复数据
res(){
    for((i=0;i<10;i++)); do
        rand4
    done
}

rand1
