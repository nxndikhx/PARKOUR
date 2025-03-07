export default function SlotCard({ vehicle, slot }) {
  return (
    <div className="bg-white text-black shadow-xl rounded-lg p-6 w-80 text-center">
      <p className="text-lg font-semibold">Vehicle Number:</p>
      <p className="text-xl mb-4">{vehicle}</p>
      <p className="text-lg font-semibold">Your Parking Slot:</p>
      <p className="text-2xl font-bold text-green-600">{slot}</p>
    </div>
  );
}
