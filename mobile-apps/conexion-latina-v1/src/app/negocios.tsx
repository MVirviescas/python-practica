import { StyleSheet, Text, View } from 'react-native';

export default function NegociosScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Negocios</Text>

      <Text style={styles.subtitle}>
        Aquí aparecerán los negocios disponibles.
      </Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },

  title: {
    fontSize: 32,
    fontWeight: 'bold',
  },

  subtitle: {
    fontSize: 18,
    marginTop: 10,
  },
});