import * as React from 'react';
import {View, Text, TextInput} from 'react-native';
import styles from './styles'


// export default TextInputWithTitle = ( {title, value, updateValue} ) => {
const  TextInputWithTitle = ( {title, placeholder, value, onChangeValue} ) => {

  return(
    <View>
      <Text>{title}</Text>
      <TextInput
        style = {styles.textInput}
        placeholder = {placeholder}
        value = {value}
        onChangeText={onChangeValue}
      />
    </View>
  )
}

export default TextInputWithTitle