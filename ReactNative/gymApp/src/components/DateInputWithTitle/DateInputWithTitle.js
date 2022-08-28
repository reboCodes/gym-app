import React, { useState } from 'react'
import { Button, Text, View } from 'react-native'
import DatePicker from 'react-native-date-picker'

export default DatePickerWithTitle = ({ title, date, open, onConfirm, onCancel, onPress }) => {

  return (
    <View>
        <Text>{title}</Text>
        <Button title={date.toISOString().substring(0, 10)} onPress={onPress} />
        <DatePicker
            modal
            mode="date"
            open={open}
            date={date}
            onConfirm={onConfirm}
            onCancel={onCancel}
        />
    </View>
  )
}