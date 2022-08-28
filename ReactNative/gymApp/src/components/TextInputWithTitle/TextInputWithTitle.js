import * as React from 'react';
import {View, Text, TextInput} from 'react-native';
import styles from './styles';


export default TextInputWithTitle = ({title}) => {
  return(
    <View>
      <Text>{title}:</Text>
      <TextInput
        style={styles.textInput}
        placeholder={title}
      />
    </View>
  )
}
