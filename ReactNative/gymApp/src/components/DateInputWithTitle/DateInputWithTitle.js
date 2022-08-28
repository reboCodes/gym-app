import React, { useState } from 'react'
import { Button, Text, View } from 'react-native'
import DatePicker from 'react-native-date-picker'

export default DatePickerWithTitle = ({title}) => {
  const [date, setDate] = useState(new Date())
  const [open, setOpen] = useState(false)

  return (
    <View>
        <Text>{title}</Text>
        <Button title={date.toISOString().substring(0, 10)} onPress={() => setOpen(true)} />
        <DatePicker
            modal
            mode="date"
            open={open}
            date={date}
            onConfirm={(date) => {
              setOpen(false)
              setDate(date)
            }}
            onCancel={() => {
              setOpen(false)
            }}
        />
    </View>
  )
}