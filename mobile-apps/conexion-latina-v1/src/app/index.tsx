import { Alert, Pressable, StyleSheet, Text, View } from 'react-native';

export default function HomeScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Conexión Latina</Text>

      <Text style={styles.subtitle}>
        Encuentra negocios latinos cerca de ti.
      </Text>

      <Pressable
        style={styles.button}
        onPress={() => Alert.alert('Conexión Latina', 'Aquí mostraremos los negocios.')}
      >
        <Text style={styles.buttonText}>Ver negocios</Text>
      </Pressable>
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

  button: {
    marginTop: 30,
    paddingHorizontal: 24,
    paddingVertical: 14,
    backgroundColor: '#222',
    borderRadius: 8,
  },

  buttonText: {
    color: 'white',
    fontSize: 16,
  },
});