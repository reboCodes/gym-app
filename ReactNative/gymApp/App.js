import * as React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

import WorkoutsScreen from './src/views/WorkoutsScreen';
import HomeScreen from './src/views/HomeScreen';
import NewWorkoutScreen from './src/views/NewWorkoutScreen';


const Stack = createNativeStackNavigator();

const App = () => {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Home">
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name="Workouts" component={WorkoutsScreen} />
        <Stack.Screen name="New Workout" component={NewWorkoutScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

export default App;