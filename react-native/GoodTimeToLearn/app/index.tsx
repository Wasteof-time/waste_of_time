import { useState } from 'react';
import { Button, StyleSheet, Text, View } from 'react-native';

export default function Index() {
    const [expression , setExpression] = useState("");
  return (
    <View style={styles.container}>
      <Text style = {styles.text}> {expression} </Text>
      <Text style = {styles.text}> Ans: {expression ? eval(expression) : 0}</Text>
      
      <View style =  {styles.buttons}>
        <Button onPress={() => {setExpression(expression + '1')}} title='1'/>
        <Button onPress={() => {setExpression(expression + '2')}} title='2'/>
        <Button onPress={() => {setExpression(expression + '3')}} title='3'/>
        <Button onPress={() => {setExpression(expression + ' + ')}} title='+'/>
      </View>
      
      <View style =  {styles.buttons}>
        <Button onPress={() => {setExpression(expression + '4')}} title='4'/>
        <Button onPress={() => {setExpression(expression + '5')}} title='5'/>
        <Button onPress={() => {setExpression(expression + '6')}} title='6'/>
        <Button onPress={() => {setExpression(expression + ' - ')}} title='-'/>
      </View>
      
      <View style =  {styles.buttons}>
        <Button onPress={() => {setExpression(expression + '7')}} title='7'/>
        <Button onPress={() => {setExpression(expression + '8')}} title='8'/>
        <Button onPress={() => {setExpression(expression + '9')}} title='9'/>
        <Button onPress={() => {setExpression(expression + ' * ')}} title='*'/>
      </View>
      
      <View style =  {styles.buttons}>
        <Button onPress={() => {setExpression(expression + '0')}} title='0'/>
      </View>
        
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  text : {
    padding : 10,
    rowGap : 10
  },
  buttons: {
    flexDirection : "row",
    paddingHorizontal : 100,
    paddingVertical : 10,
    alignItems : 'center',
    gap: 10
  }
});