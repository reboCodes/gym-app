import * as React from 'react';
import { Button, View, Text } from 'react-native';

const HomeScreen = ({ navigation }) => {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Button
        title="Workouts"
        onPress={() => {
          navigation.navigate('Workouts', { title: "asdf" });
        }}
      />
    </View>
  );
}

export default HomeScreen