import * as React from 'react';
import { Button, View, TextInput } from 'react-native';
import style from '../stylesheets/style';

const getValues = () => {
    console.log(this.state.username);
    console.log(this.state.password);
}

export default NewWorkoutScreen = ({ navigation }) => {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
        <TextInput style={style.txtinput}
            placeholder="Enter Username"
            onChangeText={(text) => this.setState({ username: text })}
        />
        <Button onPress={() => getValues()} title='Get Values' />
    </View>
  );
}

