import React, { useEffect, useState } from 'react';
import { ActivityIndicator, Button, FlatList, Text, View } from 'react-native';

export default WorkoutsScreen = ({navigation, route }) => {

  const [isLoading, setLoading] = useState(true);
  const [data, setData] = useState([]);

  const getMovies = async () => {
     try {
      const response = await fetch('http://127.0.0.1:8000/muscle');
      const json = await response.json();
      setData(json.muscles);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    getMovies();
  }, []);

  return (
    <View style={{ flex: 1, padding: 24 }}>
      {isLoading ? <ActivityIndicator/> : (
        <FlatList
          data={data}
          keyExtractor={({ muscle }, index) => muscle}
          renderItem={({ item }) => (
            <Text>{item.muscle}</Text>
          )}
        />
      )}

      <Button
        title="New Workout"
        onPress={() => {
          navigation.navigate('New Workout');
        }}
      />

    </View>
  );
};