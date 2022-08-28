import { View, Text, TextInput } from 'react-native';
import React, { useState } from 'react';
import TextInputWithTitle from '../components/TextInputWithTitle/TextInputWithTitle';
import DateInputWithTitle from '../components/DateInputWithTitle/DateInputWithTitle';

export default NewWorkoutScreen = ({ navigation }) => {

  const initialWorkoutName = "My Workout on " + new Date().toISOString().substring(0, 10)
  const [workoutName, setWorkoutName] = useState("");

  const [workoutDate, setWorkoutDate] = useState(new Date())
  const [openWorkoutDate, setOpenWorkoutDate] = useState(false)

  return (
    <View>

      <TextInputWithTitle
        title="Workout Name:"
        placeholder={initialWorkoutName}
        value={workoutName}
        onChangeValue={(newText) => {
          setWorkoutName(newText);
        }}
      />

      <Text>{workoutName}</Text>

      <DateInputWithTitle
        title={"Workout Date"}
        date={workoutDate}
        open={openWorkoutDate}
        onConfirm={(newDate) => {
          setOpenWorkoutDate(false)
          setWorkoutDate(newDate)
        }}
        onCancel={() => {setOpenWorkoutDate(false)}}
        onPress={() => setOpenWorkoutDate(true)}
      />

    </View>
  );
}



