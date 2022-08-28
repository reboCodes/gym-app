import * as React from 'react';
import { View } from 'react-native';
import TextInputWithTitle from '../components/TextInputWithTitle/TextInputWithTitle';
import DateInputWithTitle from '../components/DateInputWithTitle/DateInputWithTitle';

export default NewWorkoutScreen = ({ navigation }) => {
  return (
    <View>
      <TextInputWithTitle title={"Workout Name"}/>
      <DateInputWithTitle title={"Date"}/>
    </View>
  );
}



