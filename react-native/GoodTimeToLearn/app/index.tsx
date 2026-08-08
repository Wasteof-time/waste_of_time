import React from 'react';
import { GestureResponderEvent, ScrollView, StyleSheet, Text, TouchableOpacity, View } from 'react-native';

async function getAnswerFromThePythonServer(exp : string , getAns : any ){
    const url = 'http://localhost:8080/num';
  

  const payload = {
    user: await getUserIP(),
    exp: exp
  };

  try {

    const response = await fetch(url, {
      method: 'POST', 
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload) 
    });


    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }


    const data = await response.json();
    console.log('Success:', data);
    getAns(data.ans);
    return data;

  } catch (error) {
    console.error('Failed to execute POST request:', error);
  }
}


export default function Index() {
    const [expression , setExpression] = React.useState("");
    const [ans , setAns] = React.useState("");
    
    const handleClear = () => {
    setExpression('');
    setAns('');
    };
    interface CalcButtonProps {
      title: string;
      onPress: (event: GestureResponderEvent) => void;
      isDoubleWidth?: boolean; // The '?' means this property is optional
    }

    const CalcButton: React.FC<CalcButtonProps> = ({ title, onPress, isDoubleWidth = false }) => (
    <TouchableOpacity 
      style={[styles.button, isDoubleWidth && styles.doubleButton]} 
      onPress={onPress}
    >
      <Text style={styles.buttonText}>{title}</Text>
    </TouchableOpacity>
    );

  return (
    <ScrollView>
    <View style={styles.container}>
      <View style={styles.displayContainer}>
      <Text style = {styles.expressionText}> {expression} </Text>
      <Text style = {styles.resultText}> Ans: {ans}</Text>
      </View>
      <View style={styles.gridContainer}>
      <View style={styles.row}>
          <CalcButton onPress={() => setExpression(expression + 'sin(')} title="sin" />
          <CalcButton onPress={() => setExpression(expression + 'cos(')} title="cos" />
          <CalcButton onPress={() => setExpression(expression + 'tan(')} title="tan" />
          <CalcButton onPress={() => setExpression(expression + ')')} title=")" />
        </View>

        <View style={styles.row}>
          <CalcButton onPress={() => setExpression(expression + 'log(')} title="ln" />
          <CalcButton onPress={() => setExpression(expression + 'log10(')} title="log10" />
          <CalcButton onPress={() => setExpression(expression + ' ** ')} title="^" />
          <CalcButton onPress={() => setExpression(expression + ' % ')} title="mod" />
        </View>

        <View style={styles.row}>
          <CalcButton onPress={() => setExpression(expression + '1')} title="1" />
          <CalcButton onPress={() => setExpression(expression + '2')} title="2" />
          <CalcButton onPress={() => setExpression(expression + '3')} title="3" />
          <CalcButton onPress={() => setExpression(expression + ' + ')} title="+" />
        </View>


        <View style={styles.row}>
          <CalcButton onPress={() => setExpression(expression + '4')} title="4" />
          <CalcButton onPress={() => setExpression(expression + '5')} title="5" />
          <CalcButton onPress={() => setExpression(expression + '6')} title="6" />
          <CalcButton onPress={() => setExpression(expression + ' - ')} title="-" />
        </View>

        <View style={styles.row}>
          <CalcButton onPress={() => setExpression(expression + '7')} title="7" />
          <CalcButton onPress={() => setExpression(expression + '8')} title="8" />
          <CalcButton onPress={() => setExpression(expression + '9')} title="9" />
          <CalcButton onPress={() => setExpression(expression + ' * ')} title="*" />
        </View>

        <View style={styles.row}>
          <CalcButton onPress={() => setExpression(expression + '0')} title="0" />
          <CalcButton onPress={() => setExpression(expression + ' / ')} title="/" />
          <CalcButton onPress={() => getAnswerFromThePythonServer(expression , setAns)} title="Ans" />
          <CalcButton onPress={handleClear} title="clear" />
        </View>
        
    </View>
    </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#ffffff',
    // Calculates a stable minimum height to ensure layout takes up the full screen height inside the ScrollView
    minHeight: '100%', 
    justifyContent: 'space-between',
  },
  displayContainer: {
    flex: 1,
    minHeight: 180, // Prevents display collapse inside ScrollView
    justifyContent: 'center',
    alignItems: 'flex-end',
    paddingHorizontal: 24,
    backgroundColor: '#fafafa',
  },
  expressionText: {
    fontSize: 36,
    color: '#212121',
  },
  resultText: {
    fontSize: 24,
    color: '#757575',
    marginTop: 8,
  },
  gridContainer: {
    paddingBottom: 34, 
    paddingHorizontal: 12,
    backgroundColor: '#ffffff',
  },
  row: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 14,
  },
  button: {
    backgroundColor: '#2196F3',
    flex: 1,
    aspectRatio: 1.2,
    marginHorizontal: 4,
    borderRadius: 6,
    justifyContent: 'center',
    alignItems: 'center',
    elevation: 2,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 1 },
    shadowOpacity: 0.2,
    shadowRadius: 1.41,
  },
  doubleButton: {
    flex: 2,
    aspectRatio: 2.5,
  },
  buttonText: {
    color: '#ffffff',
    fontSize: 16,
    fontWeight: 'bold',
  },
});

async function getUserIP() {
    try {
        const response = await fetch('https://api.ipify.org?format=json');
        const data = await response.json();
        console.log("User's IP Address:", data.ip);
        return data.ip;
    } catch (error) {
        console.error("Error fetching IP address:", error);
    }
}
