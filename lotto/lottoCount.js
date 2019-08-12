const json = {'0': ['07', '08', '15', '19', '34', '38', '08'], '1': ['01', '07', '14', '16', '20', '30', '04'], '2': ['11', '24', '25', '31', '32', '37', '08'], '3': ['04', '07', '11', '14', '29', '36', '04'], '4': ['01', '19', '23', '25', '32', '37', '02'], '5': ['02', '03', '06', '08', '13', '21', '07'], '6': ['02', '03', '14', '17', '20', '38', '03'], '7': ['10', '18', '26', '29', '30', '34', '05'], '8': ['04', '06', '16', '18', '19', '28', '02'], '9': ['05', '06', '18', '24', '25', '35', '02']}

var myobj = JSON.parse(JSON.stringify(json));

const idList = Object.keys(myobj);
const nameList = Object.values(myobj);

const resultArr = [].concat.apply([],nameList).sort()

let map = new Map();
for(var i =0; i< resultArr.length; i++) {
    if(map.get(resultArr[i]) == undefined) {

        map.set(resultArr[i], 0)
    }else{
        map.set(resultArr[i], map.get(resultArr[i])+1)
    }
}

console.log(map)


