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
#这种符合条件就输出结果，猜拳的方式，那么结果就会有很多行
rand3(){
   local seeds=`while read line; do echo ${line// /..}; done <a.txt`
   seeds=`for seed in $seeds;do (( $RANDOM % 2 )) && echo $seed; done`
   echo "$seeds"
}
#继续缩小取数范围：只取1行数据
#从每次的结果集中继续猜拳，直到只有一行数据
#会出现剩下2行数据都没猜拳成功，导致输出空结果的情况，
#解决方案：如果为空，重新来一轮
rand4(){
   local seeds=`while read line; do echo ${line// /..}; done <a.txt`
   local count=0
   while [[ $count != 1 ]];do
        seeds=`for seed in $seeds;do (( $RANDOM % 2 )) && echo $seed; done`
        count=`echo "$seeds"|wc -l`
   done
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
        tmp=`rand4`
        while [[ `is_repeat $tmp` == 1 ]];do
            tmp=`rand4`
        done
        arrs[i]=$tmp
    done
    echo ${arrs[@]}
}
#判断传入的参数是否在数组中，是的话返回1
is_repeat(){
    for arr in ${arrs[@]}; do
        if [[ $arr == $1 ]];then
            echo 1
            return 1
         fi
    done
    echo 0
}

res